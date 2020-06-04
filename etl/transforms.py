class AbstractSheet:

    # These are the functions for the abstract class 
    def __init__(self, partnerId, reportNameProvided, customerName, forecastName, mfgPartno, reservedQuantity, availQuantity, boQty, age, poEta, oemPo, currency):
        self.partnerId = partnerId
        self.reportNameProvided = reportNameProvided
        self.customerName = customerName
        self.forecastName = forecastName
        self.mfgPartno = mfgPartno
        self.reservedQuantity = reservedQuantity
        self.availQuantity = availQuantity
        self.boQty = boQty
        self.age = age
        self.poEta = poEta 
        self.oemPo = oemPo
        # self.customerId = customerId
        self.currency = currency

    @staticmethod
    def keys():
        """
        Register names of common fields in this method.
        :return: List of field names
        """
        return ['partnerId', 'reportNameProvided', 'customerName', 'forecastName', 'mfgPartno', 'reservedQuantity', 'availQuantity', 'boQty', 'age', 'poEta', 'oemPo', 'currency']

    def values(self):
        return self.__dict__
    
    def __del__(self):
        '''
        This (Magic/Dunder) method deletes the object from memory
        '''
        pass
    
    def nonempty(self):
        return any((self.customerName, self.mfgPartno))
    # partnerId, reportNameProvided, customerName, forecastName, mfgPartno, reservedQuantity, availQuantity, boQty, age, poEta, oemPo, customerId, currency

class CADTechData(AbstractSheet):
    '''
    This is the class used to create objects form the Tech Data file: CADTechData  
    Mapping columns from file: 
                                customerName        = [Cust PO#] "E"
                                forecastName        = [Comments] "Z"
                                mfg Part            = [Manuf.PN] "J"
                                Reserved Quantity   = [Original Order Qty] = "O"
                                Avail Qty           = [Alloc] "Q"
                                B/O Qty             = [B/O] "R"
                                Age                 = [Age] = "N"
                                PO ETA              = [ETA] "S"
                                OEMPO               = [PO #] "T"
    '''
    def __init__(self, customerName, forecastName, mfgPartno, reservedQuantity, availQuantity, boQty, age, poEta, oemPo):
        super(CADTechData, self).__init__(customerName = customerName,
                                          forecastName = forecastName,
                                          mfgPartno = mfgPartno,
                                          reservedQuantity = reservedQuantity,
                                          availQuantity = availQuantity,
                                          boQty = boQty,
                                          age = age,
                                          poEta = poEta,
                                          oemPo = oemPo,
                                          # Missing attributes
                                          partnerId = 'Tech Data',
                                          reportNameProvided = 'DBI_LOAD_0001_CAD_TECH_DATA',
                                        #   customerId = '',
                                          currency = 'CAD')

class CADTechDataOG(AbstractSheet):
    '''
    This is the class used to create objects form the Tech Data file: CADTechDataOG  
    Mapping columns from file: 
                                customerName        = [Cust PO#] "E"
                                forecastName        = [Comments] "X"
                                mfg Part            = [Manuf.PN] "I"
                                Reserved Quantity   = [Original Order Qty] = "N"
                                Avail Qty           = [Alloc] "P"
                                B/O Qty             = [B/O] "Q"
                                Age                 = [Age] "M"
                                PO ETA              = [ETA] "R"
                                OEMPO               = [PM#] "S"
    '''
    # This is the constructor of the class
    def __init__(self, customerName, forecastName, mfgPartno, reservedQuantity, availQuantity, boQty, age, poEta, oemPo):
        super(CADTechDataOG, self).__init__(customerName = customerName,
                                            forecastName = forecastName,
                                            mfgPartno = mfgPartno,
                                            reservedQuantity = reservedQuantity,
                                            availQuantity = availQuantity,
                                            boQty = boQty,
                                            age = age,
                                            poEta = poEta,
                                            oemPo = oemPo,
                                            # Missing attributes
                                            partnerId = 'Gov Tech Data',
                                            reportNameProvided = 'DBI_LOAD_0002_CAD_Gov_Tech_Data',
                                            # customerId = '',
                                            currency = 'CAD')

class IngramMicroBMO(AbstractSheet):
    '''
    This is the class used to create objects form the Ingram file: Ingram Micro BMO  
    Mapping columns from file: 
                                mfg Part            = [MFR-PART-NBR] "C"
                                Avail Qty           = [ACTUAL QTY AVIAL] "J"
                                B/O Qty             = [QTY ON ORDER] "F"
    '''
    def __init__(self, mfgPartno, availQuantity, boQty):
        super(IngramMicroBMO, self).__init__(mfgPartno = mfgPartno,
                                          availQuantity = availQuantity,
                                          boQty = boQty,
                                          # Missing attributes
                                          partnerId = 'Ingram Micro BMO',
                                          reportNameProvided = 'DBI_LOAD_0003_Ingram_Micro_BMO',
                                          customerName = 'BMO',
                                          forecastName = '',
                                          reservedQuantity = '',
                                          age = '',
                                          poEta = '',
                                          oemPo = '', 
                                        #   customerId = '',
                                          currency = 'USD')

class Synnex(AbstractSheet):
    '''
    This is the class used to create objects from Synnex file: SynnexCUCLenovoForecastRIORecap
    Mapping columns from file:
                                customerName        = [cust_name] "I"
                                forecastname        = [RIO_reference] "H"
                                Mfg Part            = [mfg_partno] "F"
                                Reserved Quantity   = [Forecast] = "J"
                                Avail Qty           = [Quantity available] "O"
                                B/O Qty             = [On Back order] "P"
                                Age                 = [days_on_hold] = "S"
                                PO ETA              = [PO_ETA] "T"
                                OEM PO              = [SAP_no] "U"
    '''
    # This is the constructor of the class
    def __init__(self, customerName, forecastName, mfgPartno, reservedQuantity, availQuantity, boQty, age, poEta, oemPo):
        super(Synnex, self).__init__(customerName = customerName,
                                     forecastName = forecastName,
                                     mfgPartno = mfgPartno,
                                     reservedQuantity = reservedQuantity,
                                     availQuantity = availQuantity,
                                     boQty = boQty,
                                     age = age,
                                     poEta = poEta, 
                                     oemPo = oemPo,
                                    # Missing attributes
                                     partnerId = 'Synnex',
                                     reportNameProvided = 'DBI_LOAD_0004_SYNNEX',
                                    #  customerId = '',
                                     currency = 'USD')

class Ingram(AbstractSheet):
    '''
    This is the class used to create objects from Synnex file: SynnexCUCLenovoForecastRIORecap
    Mapping columns from file:
                                customerName        = [Comments] "K"
                                Mfg Part            = [Mfg Part#] "C"
                                Reserved Quantity   = [Res Qty] = "H"
                                Avail Qty           = [Avail Qty] "J"
    '''
    def __init__(self, customerName, mfgPartno, reservedQuantity, availQuantity):
        super(Ingram, self).__init__(customerName = customerName,
                                     mfgPartno = mfgPartno,
                                     reservedQuantity = reservedQuantity,
                                     availQuantity = availQuantity,
                                    #  Missing attributes
                                     partnerId = 'Ingram Micro',
                                     forecastName = '',
                                     reportNameProvided = 'DBI_LOAD_0005_Ingram_Micro',
                                     boQty = '', 
                                     age = '', 
                                     poEta = '', 
                                     oemPo = '', 
                                    #  customerId = '',
                                     currency = 'USD')
                                    
class TechData(AbstractSheet):
    '''
    This is the class used to create objects form the Tech Data file: TechDataCompucomReserveReport
    Mapping columns from file: 
                                customerName = [Customer PO number] "I"
                                forcastName  = [Customer PO number] "I" Has to be parsed out
                                mfg Part     = [Mfr Part Number (MD)] "N"
                                Avail Qty    = [Order Qty Avail to Ship] "Z"
                                B/O Qty      = [Backorder Quantity] "AA"
    '''
    # This is the constructor of the class
    def __init__(self, customerName, forecastName, mfgPartno, availQuantity, boQty):
        super(TechData, self).__init__(customerName = customerName,
                                       forecastName = forecastName,
                                       mfgPartno = mfgPartno,
                                       availQuantity = availQuantity,
                                       boQty = boQty,
                                     # Missing attributes   
                                       partnerId = 'TECH DATA',
                                       reportNameProvided = 'DBI_LOAD_0007_TECH_DATA',
                                       reservedQuantity = '',
                                       age = '', 
                                       poEta = '', 
                                       oemPo = '',
                                    #    customerId = '',
                                       currency = 'USD')

class IngramCAD(AbstractSheet):
    '''
    This is the class used to create objects form the Tech Data file: IngramCADCompucomAgedCTO
    Mapping columns from file: 
                                customerName = [Vendor Name] "D"
                                mfg Part     = [Vendor Part No] "F"
                                Avail Qty    = [Total Inventory (units)] "J"
    '''
    # This is the constructor of the class
    def __init__(self, customerName, mfgPartno, availQuantity):
        super(IngramCAD, self).__init__(customerName = customerName,
                                       mfgPartno = mfgPartno,
                                       availQuantity = availQuantity,
                                     # Missing attributes
                                       partnerId = 'Ingram Micro',
                                       forecastName = '',
                                       reportNameProvided = 'DBI_LOAD_0008_CAD_Ingram_Micro',
                                       reservedQuantity = '',
                                       boQty = '',   
                                       age = '', 
                                       poEta = '', 
                                       oemPo = '',
                                    #    customerId = '',
                                       currency = 'CAD')
