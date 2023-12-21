# CardComponentHelper.TryGetUserInfo - метод
Возвращает информацию о пользователе по объекту сессии или false, если
информацию невозможно получить.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetUserInfo(
    	ISession session,
    	out Guid userID,
    	out string userName
    )
VB __Копировать
     Public Shared Function TryGetUserInfo ( 
    	session As ISession,
    	<OutAttribute> ByRef userID As Guid,
    	<OutAttribute> ByRef userName As String
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetUserInfo(
    	ISession^ session, 
    	[OutAttribute] Guid% userID, 
    	[OutAttribute] String^% userName
    )
F# __Копировать
     static member TryGetUserInfo : 
            session : ISession * 
            userID : Guid byref * 
            userName : string byref -> bool 
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Объект сессии.
userID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор пользователя, полученное из объекта сессии.
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя пользователя, полученное из объекта сессии.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если информация о пользователе была успешно получена; false, если при
получении информации возникли проблемы.
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
