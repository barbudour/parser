# CardHelper.GetWebFileLink - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetWebFileLink(
    	string webAddress,
    	Guid? cardID = null,
    	Guid? fileID = null,
    	Guid? versionID = null,
    	Guid? cardTypeID = null,
    	string cardTypeName = null,
    	string fileName = null,
    	string fileTypeName = null,
    	bool asHtml = true,
    	bool normalize = true
    )
VB __Копировать
     Public Shared Function GetWebFileLink ( 
    	webAddress As String,
    	Optional cardID As Guid? = Nothing,
    	Optional fileID As Guid? = Nothing,
    	Optional versionID As Guid? = Nothing,
    	Optional cardTypeID As Guid? = Nothing,
    	Optional cardTypeName As String = Nothing,
    	Optional fileName As String = Nothing,
    	Optional fileTypeName As String = Nothing,
    	Optional asHtml As Boolean = true,
    	Optional normalize As Boolean = true
    ) As String
C++ __Копировать
     public:
    static String^ GetWebFileLink(
    	String^ webAddress, 
    	Nullable<Guid> cardID = nullptr, 
    	Nullable<Guid> fileID = nullptr, 
    	Nullable<Guid> versionID = nullptr, 
    	Nullable<Guid> cardTypeID = nullptr, 
    	String^ cardTypeName = nullptr, 
    	String^ fileName = nullptr, 
    	String^ fileTypeName = nullptr, 
    	bool asHtml = true, 
    	bool normalize = true
    )
F# __Копировать
     static member GetWebFileLink : 
            webAddress : string * 
            ?cardID : Nullable<Guid> * 
            ?fileID : Nullable<Guid> * 
            ?versionID : Nullable<Guid> * 
            ?cardTypeID : Nullable<Guid> * 
            ?cardTypeName : string * 
            ?fileName : string * 
            ?fileTypeName : string * 
            ?asHtml : bool * 
            ?normalize : bool 
    (* Defaults:
            let _cardID = defaultArg cardID null
            let _fileID = defaultArg fileID null
            let _versionID = defaultArg versionID null
            let _cardTypeID = defaultArg cardTypeID null
            let _cardTypeName = defaultArg cardTypeName null
            let _fileName = defaultArg fileName null
            let _fileTypeName = defaultArg fileTypeName null
            let _asHtml = defaultArg asHtml true
            let _normalize = defaultArg normalize true
    *)
    -> string 
#### Параметры
webAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
fileID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
versionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
fileTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
asHtml [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
normalize [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
