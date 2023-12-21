# CardHelper.GetLink - метод
Возвращает ссылку на открытие карточки в клиентском приложении с опциональным
открытием файла в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetLink(
    	ISession session,
    	Guid cardID,
    	Guid? fileID = null,
    	Guid? versionID = null,
    	string applicationAlias = null
    )
VB __Копировать
     Public Shared Function GetLink ( 
    	session As ISession,
    	cardID As Guid,
    	Optional fileID As Guid? = Nothing,
    	Optional versionID As Guid? = Nothing,
    	Optional applicationAlias As String = Nothing
    ) As String
C++ __Копировать
     public:
    static String^ GetLink(
    	ISession^ session, 
    	Guid cardID, 
    	Nullable<Guid> fileID = nullptr, 
    	Nullable<Guid> versionID = nullptr, 
    	String^ applicationAlias = nullptr
    )
F# __Копировать
     static member GetLink : 
            session : ISession * 
            cardID : Guid * 
            ?fileID : Nullable<Guid> * 
            ?versionID : Nullable<Guid> * 
            ?applicationAlias : string 
    (* Defaults:
            let _fileID = defaultArg fileID null
            let _versionID = defaultArg versionID null
            let _applicationAlias = defaultArg applicationAlias null
    *)
    -> string 
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Текущая сессия, из которой вычисляется код сервера.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, которая открывается по ссылке.
fileID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
Идентификатор файла, который будет открыт после открытия карточки cardID, или
null, если файл открывать не требуется.
Если параметр versionID не задан, то открывается последняя версия файла.
versionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
Идентификатор версии файла, контент которой будет открыт после открытия файла
fileID, или null, если версию открывать не требуется.
Для отличного от null значения должен быть задан параметр fileID.
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Алиас приложения или null, если используется алиас по умолчанию.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Ссылка на открытие карточки.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
