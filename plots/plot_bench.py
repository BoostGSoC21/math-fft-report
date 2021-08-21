import matplotlib.pyplot as plt

def parse_line(l):
    ls = l.split()
    t = float(ls[1])*1e-6
    name,n = ls[0].split('/')
    n = int(n)
    name = name.split('_')[1]
    return name,n,t
#bench_gsl/109          34167 ns        34166 ns        20445   

def parse(f):
    data= { 'gsl' : (list(),list()),  
        'bsl' : (list(),list()),  
        'fftw' : (list(),list()),  }
    with open(f,'r') as fd:
        for l in fd:
            name,x,y = parse_line(l)
            data[name][0].append(x)
            data[name][1].append(y)
    return data

def plot_complex(f,title,fout):
    fig= plt.figure(figsize=[5,4])
    ax = fig.subplots()
    #ax.set_title('Benchmark (%s)' % title)
    ax.text(.5,.9,title,horizontalalignment='center',transform=ax.transAxes)
    ax.set_xlabel('size')
    ax.set_ylabel('time (ms)')
    data = parse(f)
    ax.loglog( data['gsl'][0],data['gsl'][1],'-o',label='gsl',color='green')
    ax.loglog( data['bsl'][0],data['bsl'][1],'-o',label='bsl',color = 'blue')
    ax.loglog( data['fftw'][0],data['fftw'][1],'-o',label='fftw', color = 'red')
    ax.legend()
    plt.savefig(fout)
    #plt.show()

if __name__ == "__main__":
    plot_complex('complex_bench_primes.txt','prime sizes, complex DFT','complex_primes.pdf')
    plot_complex('complex_bench_p2.txt','powers of 2, complex DFT','complex_p2.pdf')
    plot_complex('complex_bench_p10.txt','powers of 10, complex DFT','complex_p10.pdf')
    
    plot_complex('real_bench_primes.txt','prime sizes, real DFT','real_primes.pdf')
    plot_complex('real_bench_p2.txt','powers of 2, real DFT','real_p2.pdf')
    plot_complex('real_bench_p10.txt','powers of 10, real DFT','real_p10.pdf')
