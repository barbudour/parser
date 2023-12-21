# FormUIExtensionContext - класс
Контекст расширений на диалоговые окна
[IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FormUIExtensionContext : IFormUIExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class FormUIExtensionContext
    	Implements IFormUIExtensionContext, IExtensionContext
C++ __Копировать
     public ref class FormUIExtensionContext sealed : IFormUIExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type FormUIExtensionContext = 
        class
            interface IFormUIExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FormUIExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IFormUIExtensionContext](T_Tessa_UI_IFormUIExtensionContext.htm)
##  __Конструкторы
[FormUIExtensionContext](M_Tessa_UI_FormUIExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Buttons](P_Tessa_UI_FormUIExtensionContext_Buttons.htm)| Список кнопок,
выводимых в отображаемом диалоге.  
---|---  
[Cancel](P_Tessa_UI_FormUIExtensionContext_Cancel.htm)| Признак того, что
отображение диалога будет отменено по завершении выполнения расширений.  
[CancellationToken](P_Tessa_UI_FormUIExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CardType](P_Tessa_UI_FormUIExtensionContext_CardType.htm)| Метаинформация по
типу карточки, который содержал форму диалога.  
[Form](P_Tessa_UI_FormUIExtensionContext_Form.htm)|  Модель представления
формы для отображаемого диалога. Содержит все элементы управления. Значение
свойства можно изменить.  
[Info](P_Tessa_UI_FormUIExtensionContext_Info.htm)| Дополнительная информация
для расширений.  
[InitializeWindowActionAsync](P_Tessa_UI_FormUIExtensionContext_InitializeWindowActionAsync.htm)|
Асинхронный метод, вызываемый для инициализации окна диалога, или null, если
метод ещё не задан. Рекомендуется добавлять новые методы оператором +=.  
[ModalDialog](P_Tessa_UI_FormUIExtensionContext_ModalDialog.htm)| Признак
того, что диалог будет отображён в модальном режиме.  
[Model](P_Tessa_UI_FormUIExtensionContext_Model.htm)| Модель карточки диалога
в UI.  
[Title](P_Tessa_UI_FormUIExtensionContext_Title.htm)| Заголовок окна диалога.
Значение свойства можно изменить.  
[TypeForm](P_Tessa_UI_FormUIExtensionContext_TypeForm.htm)|  Метаинформация по
форме типа карточки, по которой был построен UI в объекте [Form].  
[ValidationResult](P_Tessa_UI_FormUIExtensionContext_ValidationResult.htm)|
Сообщения валидации, связанные с выполняемыми расширениями. Сообщения
выводятся пользователю по завершению выполнения расширений. Если сообщения
содержат ошибки, то диалог не будет отображён.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
