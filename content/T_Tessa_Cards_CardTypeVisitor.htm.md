# CardTypeVisitor - класс
Базовый класс для объектов, выполняющих посещение объектов типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardTypeVisitor : ICardTypeVisitor
VB __Копировать
     Public MustInherit Class CardTypeVisitor
    	Implements ICardTypeVisitor
C++ __Копировать
     public ref class CardTypeVisitor abstract : ICardTypeVisitor
F# __Копировать
     [<AbstractClassAttribute>]
    type CardTypeVisitor = 
        class
            interface ICardTypeVisitor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeVisitor
Derived
[Tessa.Extensions.Default.Client.UI.FindAttachedFieldControlVisitor](T_Tessa_Extensions_Default_Client_UI_FindAttachedFieldControlVisitor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.TagParserCardTypeVisitor](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_TagParserCardTypeVisitor.htm)
[Tessa.UI.Cards.CardTypeRepairVisitor](T_Tessa_UI_Cards_CardTypeRepairVisitor.htm)
[Tessa.UI.WorkflowViewer.CardTypeParamVisitor](T_Tessa_UI_WorkflowViewer_CardTypeParamVisitor.htm)
Implements
    [ICardTypeVisitor](T_Tessa_Cards_ICardTypeVisitor.htm)
##  __Конструкторы
[CardTypeVisitor](M_Tessa_Cards_CardTypeVisitor__ctor.htm)|  Создаёт экземпляр
класса.  
---|---  
## __Свойства
[ValidationResult](P_Tessa_Cards_CardTypeVisitor_ValidationResult.htm)|
Результат валидации, полученный посредством посещения объектов типа карточки.  
---|---  
## __Методы
[BuildResultAsync](M_Tessa_Cards_CardTypeVisitor_BuildResultAsync.htm)|
Возвращает результат валидации, полученный посредством посещения объектов типа
карточки.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[VisitBlockAsync](M_Tessa_Cards_CardTypeVisitor_VisitBlockAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeBlock] в типе карточки.  
[VisitColumnAsync](M_Tessa_Cards_CardTypeVisitor_VisitColumnAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeColumn] в типе карточки.  
[VisitCompletionOptionAsync](M_Tessa_Cards_CardTypeVisitor_VisitCompletionOptionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeCompletionOption] в типе карточки.  
[VisitControlAsync](M_Tessa_Cards_CardTypeVisitor_VisitControlAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeControl] в типе карточки.  
[VisitExtensionAsync](M_Tessa_Cards_CardTypeVisitor_VisitExtensionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeExtension] в типе карточки.  
[VisitNamedFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitNamedFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeNamedForm] в типе карточки.  
[VisitSchemeItemAsync](M_Tessa_Cards_CardTypeVisitor_VisitSchemeItemAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeSchemeItem] в типе карточки.  
[VisitTabFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTabFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTabForm] в типе карточки.  
[VisitTableFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTableFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTableForm] в типе карточки.  
[VisitTypeFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTypeFormAsync.htm)|
Посещает основную форму [Tessa.Cards.CardTypeTabForm] в типе карточки.  
[VisitValidatorAsync(CardTypeValidator, CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitValidatorAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки.  
[VisitValidatorAsync(CardTypeValidator, CardTypeCompletionOption, CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitValidatorAsync_1.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки для варианта
завершения.  
## __Методы расширения
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
