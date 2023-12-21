# CheckTaskAccessHelper.CheckAccessAsync(ICardStoreTaskExtensionContext) -
метод
Метод для проверки прав доступа на изменение карточки задания
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> CheckAccessAsync(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Public Shared Function CheckAccessAsync ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    static Task<bool>^ CheckAccessAsync(
    	ICardStoreTaskExtensionContext^ context
    )
F# __Копировать
     static member CheckAccessAsync : 
            context : ICardStoreTaskExtensionContext -> Task<bool> 
#### Параметры
context
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
    Контекст расширения на сохранение задания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Возвращает true, если проверка прошла успешно.
##  __См. также
#### Ссылки
[CheckTaskAccessHelper -
](T_Tessa_Extensions_Platform_Server_Cards_CheckTaskAccessHelper.htm)
[CheckAccessAsync -
перегрузка](Overload_Tessa_Extensions_Platform_Server_Cards_CheckTaskAccessHelper_CheckAccessAsync.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
