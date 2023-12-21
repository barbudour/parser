# CardHelper.GetTaskState - метод
Возвращает строку с кратким описанием по состоянию задания по его параметрам.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetTaskState(
    	string roleName,
    	string userName,
    	Guid? completionOptionID
    )
VB __Копировать
     Public Shared Function GetTaskState ( 
    	roleName As String,
    	userName As String,
    	completionOptionID As Guid?
    ) As String
C++ __Копировать
     public:
    static String^ GetTaskState(
    	String^ roleName, 
    	String^ userName, 
    	Nullable<Guid> completionOptionID
    )
F# __Копировать
     static member GetTaskState : 
            roleName : string * 
            userName : string * 
            completionOptionID : Nullable<Guid> -> string 
#### Параметры
roleName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя роли, на которую назначено задание. Может быть локализуемой строкой. 
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя пользователя, который взял задание в работу или завершил его. Может быть локализуемой строкой. 
completionOptionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор варианта завершения задания или null, если задание ещё не было завершено. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка с кратким описанием по состоянию задания по его параметрам.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
