# IFormUIExtensionContext - интерфейс
Контекст расширений на диалоговые окна
[IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFormUIExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IFormUIExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IFormUIExtensionContext : IExtensionContext
F# __Копировать
     type IFormUIExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[Buttons](P_Tessa_UI_IFormUIExtensionContext_Buttons.htm)| Список кнопок,
выводимых в отображаемом диалоге.  
---|---  
[Cancel](P_Tessa_UI_IFormUIExtensionContext_Cancel.htm)| Признак того, что
отображение диалога будет отменено по завершении выполнения расширений.  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[CardType](P_Tessa_UI_IFormUIExtensionContext_CardType.htm)| Метаинформация по
типу карточки, который содержал форму диалога.  
[Form](P_Tessa_UI_IFormUIExtensionContext_Form.htm)|  Модель представления
формы для отображаемого диалога. Содержит все элементы управления. Значение
свойства можно изменить.  
[Info](P_Tessa_UI_IFormUIExtensionContext_Info.htm)| Дополнительная информация
для расширений.  
[InitializeWindowActionAsync](P_Tessa_UI_IFormUIExtensionContext_InitializeWindowActionAsync.htm)|
Асинхронный метод, вызываемый для инициализации окна диалога, или null, если
метод ещё не задан. Рекомендуется добавлять новые методы оператором +=.  
[ModalDialog](P_Tessa_UI_IFormUIExtensionContext_ModalDialog.htm)| Признак
того, что диалог будет отображён в модальном режиме.  
[Model](P_Tessa_UI_IFormUIExtensionContext_Model.htm)| Модель карточки диалога
в UI.  
[Title](P_Tessa_UI_IFormUIExtensionContext_Title.htm)| Заголовок окна диалога.
Значение свойства можно изменить.  
[TypeForm](P_Tessa_UI_IFormUIExtensionContext_TypeForm.htm)|  Метаинформация
по форме типа карточки, по которой был построен UI в объекте [Form].  
[ValidationResult](P_Tessa_UI_IFormUIExtensionContext_ValidationResult.htm)|
Сообщения валидации, связанные с выполняемыми расширениями. Сообщения
выводятся пользователю по завершению выполнения расширений. Если сообщения
содержат ошибки, то диалог не будет отображён.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
