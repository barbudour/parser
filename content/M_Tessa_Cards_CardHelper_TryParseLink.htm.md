# CardHelper.TryParseLink - метод
Выполняет попытку прочитать параметры, полученные для открытия карточки по
ссылке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryParseLink(
    	Dictionary<string, string> parameters,
    	out Guid cardID,
    	out string displayValue,
    	out Guid? fileID,
    	out Guid? versionID
    )
VB __Копировать
     Public Shared Function TryParseLink ( 
    	parameters As Dictionary(Of String, String),
    	<OutAttribute> ByRef cardID As Guid,
    	<OutAttribute> ByRef displayValue As String,
    	<OutAttribute> ByRef fileID As Guid?,
    	<OutAttribute> ByRef versionID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    static bool TryParseLink(
    	Dictionary<String^, String^>^ parameters, 
    	[OutAttribute] Guid% cardID, 
    	[OutAttribute] String^% displayValue, 
    	[OutAttribute] Nullable<Guid>% fileID, 
    	[OutAttribute] Nullable<Guid>% versionID
    )
F# __Копировать
     static member TryParseLink : 
            parameters : Dictionary<string, string> * 
            cardID : Guid byref * 
            displayValue : string byref * 
            fileID : Nullable<Guid> byref * 
            versionID : Nullable<Guid> byref -> bool 
#### Параметры
parameters
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
    Параметры, полученные для открытия карточки по ссылке.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, которая открывается по ссылке.
displayValue [String](https://learn.microsoft.com/dotnet/api/system.string)
     Отображаемое имя вкладки с открываемой карточкой. Значение обычно используется при отсутствии у карточки Digest. 
fileID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
Идентификатор файла, который будет открыт после открытия карточки cardID, или
null, если файл открывать не требуется.
Если параметр versionID не задан, то открывается последняя версия файла.
versionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
Идентификатор версии файла, контент которой будет открыт после открытия файла
fileID, или null, если версию открывать не требуется.
Для отличного от null значения должен быть задан параметр fileID.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если параметры удалось прочитать; false в противном случае.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
