# CardTableViewControlViewModel.EditRowCommand - свойство
Команда, выполняемая при открытии окна редактирования строки (например, по
двойному клику). Команду нельзя изменить в расширениях, используйте событие
[RowInvoked](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInvoked.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ICommand EditRowCommand { get; }
VB __Копировать
     Public ReadOnly Property EditRowCommand As ICommand
    	Get
C++ __Копировать
     public:
    property ICommand^ EditRowCommand {
    	ICommand^ get ();
    }
F# __Копировать
     member EditRowCommand : ICommand with get
#### Значение свойства
[ICommand](https://learn.microsoft.com/dotnet/api/system.windows.input.icommand)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
