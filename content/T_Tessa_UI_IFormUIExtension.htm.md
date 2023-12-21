# IFormUIExtension - интерфейс
Расширение на диалоговое окно. Вызывается для методов
[ShowFormDialogAsync(String, CardTypeForm, ICardModel, Func<IFormViewModel,
CancellationToken, ValueTask>, Func<Window, CancellationToken, ValueTask>,
Boolean, Boolean, Boolean, CancellationToken,
UIButton[])](M_Tessa_UI_IUIHost_ShowFormDialogAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFormUIExtension : IExtension
VB __Копировать
     Public Interface IFormUIExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IFormUIExtension : IExtension
F# __Копировать
     type IFormUIExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[Initialized](M_Tessa_UI_IFormUIExtension_Initialized.htm)| Отображает
диалоговое окно с выбором объекта среди всех доступных представлениям.  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
