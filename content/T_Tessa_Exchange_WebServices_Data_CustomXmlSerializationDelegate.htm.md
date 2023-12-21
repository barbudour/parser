# CustomXmlSerializationDelegate - делегат
Defines a delegate that is used to allow applications to emit custom XML when
SOAP requests are sent to Exchange.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void CustomXmlSerializationDelegate(
    	XmlWriter writer
    )
VB __Копировать
     Public Delegate Sub CustomXmlSerializationDelegate ( 
    	writer As XmlWriter
    )
C++ __Копировать
     public delegate void CustomXmlSerializationDelegate(
    	XmlWriter^ writer
    )
F# __Копировать
     type CustomXmlSerializationDelegate = 
        delegate of 
            writer : XmlWriter -> unit
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    The XmlWriter to use to emit the custom XML.
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
