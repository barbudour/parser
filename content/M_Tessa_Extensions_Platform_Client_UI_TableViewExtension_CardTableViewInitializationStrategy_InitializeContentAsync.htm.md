# CardTableViewInitializationStrategy.InitializeContentAsync - метод
Убираем ненужные кнопки и копируем кнопки дял пейджинга из верхней панели в
нижнюю.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask InitializeContentAsync(
    	CardViewControlInitializationContext context
    )
VB __Копировать
     Public Overrides Function InitializeContentAsync ( 
    	context As CardViewControlInitializationContext
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask InitializeContentAsync(
    	CardViewControlInitializationContext^ context
    ) override
F# __Копировать
     abstract InitializeContentAsync : 
            context : CardViewControlInitializationContext -> ValueTask 
    override InitializeContentAsync : 
            context : CardViewControlInitializationContext -> ValueTask 
#### Параметры
context
[CardViewControlInitializationContext](T_Tessa_UI_Cards_Controls_CardViewControlInitializationContext.htm)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
#### Реализации
[IViewCardControlInitializationStrategy.InitializeContentAsync(CardViewControlInitializationContext)](M_Tessa_UI_Cards_Controls_IViewCardControlInitializationStrategy_InitializeContentAsync.htm)  
##  __См. также
#### Ссылки
[CardTableViewInitializationStrategy -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewInitializationStrategy.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
