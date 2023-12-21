# ContainmentMode - перечисление
Defines the containment mode for Contains search filters.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ContainmentMode
VB __Копировать
     Public Enumeration ContainmentMode
C++ __Копировать
     public enum class ContainmentMode
F# __Копировать
     type ContainmentMode
##  __Члены
FullString| 0|  The comparison is between the full string and the constant.
The property value and the supplied constant are precisely the same.  
---|---|---  
Prefixed| 1|  The comparison is between the string prefix and the constant.  
Substring| 2|  The comparison is between a substring of the string and the
constant.  
PrefixOnWords| 3|  The comparison is between a prefix on individual words in
the string and the constant.  
ExactPhrase| 4|  The comparison is between an exact phrase in the string and
the constant.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
