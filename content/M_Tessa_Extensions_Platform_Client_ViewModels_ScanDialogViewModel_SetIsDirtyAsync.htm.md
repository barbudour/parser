# ScanDialogViewModel.SetIsDirtyAsync - метод
Устанавливает значение свойства
[IsDirty](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_IsDirty.htm)
асинхронно. Метод можно вызывать не из потока UI.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetIsDirtyAsync(
    	bool value
    )
VB __Копировать
     Public Function SetIsDirtyAsync ( 
    	value As Boolean
    ) As Task
C++ __Копировать
     public:
    Task^ SetIsDirtyAsync(
    	bool value
    )
F# __Копировать
     member SetIsDirtyAsync : 
            value : bool -> Task 
#### Параметры
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что диалог содержит изменения, которые надо сохранить.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ScanDialogViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
