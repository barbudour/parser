# CardTemporaryRole - конструктор
Создаёт экземпляр класса с указанием роли задания и контекста её получения из
контекстной роли.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTemporaryRole(
    	TaskRole taskRole,
    	DateTime storeDateTime,
    	int? plannedQuants,
    	Guid contextRoleID,
    	string contextRoleName,
    	string contextSqlTextForCard,
    	Guid cardID
    )
VB __Копировать
     Public Sub New ( 
    	taskRole As TaskRole,
    	storeDateTime As DateTime,
    	plannedQuants As Integer?,
    	contextRoleID As Guid,
    	contextRoleName As String,
    	contextSqlTextForCard As String,
    	cardID As Guid
    )
C++ __Копировать
     public:
    CardTemporaryRole(
    	TaskRole^ taskRole, 
    	DateTime storeDateTime, 
    	Nullable<int> plannedQuants, 
    	Guid contextRoleID, 
    	String^ contextRoleName, 
    	String^ contextSqlTextForCard, 
    	Guid cardID
    )
F# __Копировать
     new : 
            taskRole : TaskRole * 
            storeDateTime : DateTime * 
            plannedQuants : Nullable<int> * 
            contextRoleID : Guid * 
            contextRoleName : string * 
            contextSqlTextForCard : string * 
            cardID : Guid -> CardTemporaryRole
#### Параметры
taskRole [TaskRole](T_Tessa_Roles_TaskRole.htm)
    Роль задания. Не может быть равна null.
storeDateTime
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Время сохранения.
plannedQuants
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
    Количество квантов на задание.
contextRoleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор контекстной роли.
contextRoleName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя контекстной роли.
contextSqlTextForCard
[String](https://learn.microsoft.com/dotnet/api/system.string)
    SQL-запрос для получения состава контекстной роли.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор сохраняемой карточки.
##  __См. также
#### Ссылки
[CardTemporaryRole - ](T_Tessa_Cards_ComponentModel_CardTemporaryRole.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
