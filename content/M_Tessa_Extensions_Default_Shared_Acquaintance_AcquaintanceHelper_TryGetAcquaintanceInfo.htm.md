# AcquaintanceHelper.TryGetAcquaintanceInfo - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Acquaintance](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void TryGetAcquaintanceInfo(
    	Dictionary<string, Object> info,
    	out IList roleList,
    	out string comment,
    	out bool excludeDeputies,
    	out string placeholderAliases,
    	out Dictionary<string, Object> additionalInfo,
    	out bool addSuccessMessage
    )
VB __Копировать
     Public Shared Sub TryGetAcquaintanceInfo ( 
    	info As Dictionary(Of String, Object),
    	<OutAttribute> ByRef roleList As IList,
    	<OutAttribute> ByRef comment As String,
    	<OutAttribute> ByRef excludeDeputies As Boolean,
    	<OutAttribute> ByRef placeholderAliases As String,
    	<OutAttribute> ByRef additionalInfo As Dictionary(Of String, Object),
    	<OutAttribute> ByRef addSuccessMessage As Boolean
    )
C++ __Копировать
     public:
    static void TryGetAcquaintanceInfo(
    	Dictionary<String^, Object^>^ info, 
    	[OutAttribute] IList^% roleList, 
    	[OutAttribute] String^% comment, 
    	[OutAttribute] bool% excludeDeputies, 
    	[OutAttribute] String^% placeholderAliases, 
    	[OutAttribute] Dictionary<String^, Object^>^% additionalInfo, 
    	[OutAttribute] bool% addSuccessMessage
    )
F# __Копировать
     static member TryGetAcquaintanceInfo : 
            info : Dictionary<string, Object> * 
            roleList : IList byref * 
            comment : string byref * 
            excludeDeputies : bool byref * 
            placeholderAliases : string byref * 
            additionalInfo : Dictionary<string, Object> byref * 
            addSuccessMessage : bool byref -> unit 
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
roleList
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
comment [String](https://learn.microsoft.com/dotnet/api/system.string)
excludeDeputies
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
placeholderAliases
[String](https://learn.microsoft.com/dotnet/api/system.string)
additionalInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
addSuccessMessage
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
## __См. также
#### Ссылки
[AcquaintanceHelper -
](T_Tessa_Extensions_Default_Shared_Acquaintance_AcquaintanceHelper.htm)
[Tessa.Extensions.Default.Shared.Acquaintance - пространство
имён](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)
