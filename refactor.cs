public static void Test(List<Ins> ins, List<C> b, DateTime day)
{
	if ((ins != null) && (ins.count > 0) && (b != null)){
        foreach (var i in ins.Where(x => x.ty == "O"))
        {
            bool ex = false;
		    bool ef = false;
            if (i.date == 9999)
            {
                ex = true;
            }

            var m = b.Where(ba => ba.ted <= i.bexd);
            foreach (var bl in m)
            {
                switch (1)
                {
                    case 1 when bl.ted == i.bexd:
                        ex = true;
                        break;
                    case 1 when (bl.ted > i.befd && bl.ted < i.bexd):
                        if (!ex)
                        {
                            console.writeline("A");
                            ex = true;
                        }
                        console.writeline("B");
                        break;
                    case 1 when bl.ted == i.befd:
                        if (!ex)
                        {
                            console.writeline("C");
                            ex = true;
                        }
                        console.writeline("D");
                        ef = true;
                        break;
                    case 1 when bl.ted < i.befd:
                        if (!ex)
                        {
                            console.writeline("E");
                            ex = true;
                        }
                        if (!ef)
                        {
                            if (bl.ted > day)
                            {
                                console.writeline("F");
                                ef = true;
                            }
                            else if (bl.ted < day)
                            {
                                console.writeline("G");
                                ef = true;
                            } 
                        }
                        
                        break;
                }
            }
            if (!ex)
            {
                console.writeline("H");
            }
            if (!ef)
            {
                console.writeline("I");
            }
        }

    }
		
		
		