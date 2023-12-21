# CardTableViewControlViewModel.InternalRefreshAsync - метод
Новый рефреш представления с учетом того, что это теперь таблица.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask InternalRefreshAsync(
    	IDisposable uiLockLifetime
    )
VB __Копировать
     Protected Overrides Function InternalRefreshAsync ( 
    	uiLockLifetime As IDisposable
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask InternalRefreshAsync(
    	IDisposable^ uiLockLifetime
    ) override
F# __Копировать
     abstract InternalRefreshAsync : 
            uiLockLifetime : IDisposable -> ValueTask 
    override InternalRefreshAsync : 
            uiLockLifetime : IDisposable -> ValueTask 
#### Параметры
uiLockLifetime
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
