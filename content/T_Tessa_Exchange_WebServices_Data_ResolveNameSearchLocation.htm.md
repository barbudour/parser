# ResolveNameSearchLocation - перечисление
Defines the location where a ResolveName operation searches for contacts.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ResolveNameSearchLocation
VB __Копировать
     Public Enumeration ResolveNameSearchLocation
C++ __Копировать
     public enum class ResolveNameSearchLocation
F# __Копировать
     type ResolveNameSearchLocation
##  __Члены
DirectoryOnly| 0|  The name is resolved against the Global Address List.  
---|---|---  
DirectoryThenContacts| 1|  The name is resolved against the Global Address
List and then against the Contacts folder if no match was found.  
ContactsOnly| 2|  The name is resolved against the Contacts folder.  
ContactsThenDirectory| 3|  The name is resolved against the Contacts folder
and then against the Global Address List if no match was found.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
