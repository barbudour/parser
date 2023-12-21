# CardTableViewControlViewModel.ApplyClientQuickSearch - метод
Перегузка дефолтного клиентского поиска. Так как клиентский поиск должен
работать с пейджингом, филтрация происходит в
[InternalRefreshAsync(IDisposable)](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_InternalRefreshAsync.htm),
а не в фильтре [TreeCollectionView](T_Tessa_UI_Data_TreeCollectionView.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override void ApplyClientQuickSearch(
    	string text
    )
VB __Копировать
     Public Overrides Sub ApplyClientQuickSearch ( 
    	text As String
    )
C++ __Копировать
     public:
    virtual void ApplyClientQuickSearch(
    	String^ text
    ) override
F# __Копировать
     abstract ApplyClientQuickSearch : 
            text : string -> unit 
    override ApplyClientQuickSearch : 
            text : string -> unit 
#### Параметры
text [String](https://learn.microsoft.com/dotnet/api/system.string)
## __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
