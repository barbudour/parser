# EffectiveRights - перечисление
Defines the effective user rights associated with an item or folder.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum EffectiveRights
VB __Копировать
    <FlagsAttribute>
    Public Enumeration EffectiveRights
C++ __Копировать
    [FlagsAttribute]
    public enum class EffectiveRights
F# __Копировать
     [<FlagsAttribute>]
    type EffectiveRights
##  __Члены
None| 0|  The user has no acces right on the item or folder.  
---|---|---  
CreateAssociated| 1|  The user can create associated items (FAI)  
CreateContents| 2|  The user can create items.  
CreateHierarchy| 4|  The user can create sub-folders.  
Delete| 8|  The user can delete items and/or folders.  
Modify| 16|  The user can modify the properties of items and/or folders.  
Read| 32|  The user can read the contents of items.  
ViewPrivateItems| 64|  The user can view private items.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
