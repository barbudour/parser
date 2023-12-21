# IApplicationCollectionUpdater.UpdateApplicationsAsync - метод
Осуществляет обновление приложений в коллекции приложений для каталога catalog
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    Task UpdateApplicationsAsync(
    	[NotNullAttribute] IApplicationCatalog catalog
    )
VB __Копировать
    <NotNullAttribute>
    Function UpdateApplicationsAsync ( 
    	<NotNullAttribute> catalog As IApplicationCatalog
    ) As Task
C++ __Копировать
    [NotNullAttribute]
    Task^ UpdateApplicationsAsync(
    	[NotNullAttribute] IApplicationCatalog^ catalog
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract UpdateApplicationsAsync : 
            [<NotNullAttribute>] catalog : IApplicationCatalog -> Task 
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Каталог приложений 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Задача обновления
## __См. также
#### Ссылки
[IApplicationCollectionUpdater -
](T_Tessa_Applications_IApplicationCollectionUpdater.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
