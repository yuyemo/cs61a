def cy2(x):
        return x
def cycle(f1,f2,f3):
        def cy1(n):
            def cy3(x):
                i=n%3
                p=n//3
                if p>=1:
                    t=0
                    while t<p:
                        cy2=f3(f2(f1(cy2(x))))
                        t+=1
                if i==1:
                    cy2=f1(cy2)
                if i==2:
                    cy2=f2(cy2)
                return cy2
            return cy3
        return cy1

