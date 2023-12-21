# TagParserCardTypeVisitor - класс
Помощник переноса тэгов в формате [Tag1],..,[TagN] из имён блоков и контролов
в настройки блока/контрола (TagsListSetting). Также удаляет тэги из имени
элемента.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public class TagParserCardTypeVisitor : CardTypeVisitor
VB __Копировать
     Public Class TagParserCardTypeVisitor
    	Inherits CardTypeVisitor
C++ __Копировать
     public ref class TagParserCardTypeVisitor : public CardTypeVisitor
F# __Копировать
     type TagParserCardTypeVisitor = 
        class
            inherit CardTypeVisitor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm) __ TagParserCardTypeVisitor
##  __Конструкторы
[TagParserCardTypeVisitor](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_TagParserCardTypeVisitor__ctor.htm)|
Создаёт экземпляр класса.  
---|---  
## __Свойства
[ValidationResult](P_Tessa_Cards_CardTypeVisitor_ValidationResult.htm)|
Результат валидации, полученный посредством посещения объектов типа карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
---|---  
##  __Методы
[BuildResultAsync](M_Tessa_Cards_CardTypeVisitor_BuildResultAsync.htm)|
Возвращает результат валидации, полученный посредством посещения объектов типа
карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
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
[VisitBlockAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_TagParserCardTypeVisitor_VisitBlockAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeBlock] в типе карточки.  
(Переопределяет [CardTypeVisitor.VisitBlockAsync(CardTypeBlock, CardTypeForm,
CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitBlockAsync.htm))  
[VisitColumnAsync](M_Tessa_Cards_CardTypeVisitor_VisitColumnAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeColumn] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitCompletionOptionAsync](M_Tessa_Cards_CardTypeVisitor_VisitCompletionOptionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeCompletionOption] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitControlAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_TagParserCardTypeVisitor_VisitControlAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeControl] в типе карточки.  
(Переопределяет [CardTypeVisitor.VisitControlAsync(CardTypeControl,
CardTypeBlock, CardTypeForm, CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitControlAsync.htm))  
[VisitExtensionAsync](M_Tessa_Cards_CardTypeVisitor_VisitExtensionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeExtension] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitNamedFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitNamedFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeNamedForm] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitSchemeItemAsync](M_Tessa_Cards_CardTypeVisitor_VisitSchemeItemAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeSchemeItem] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitTabFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTabFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTabForm] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitTableFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTableFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTableForm] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitTypeFormAsync](M_Tessa_Cards_CardTypeVisitor_VisitTypeFormAsync.htm)|
Посещает основную форму [Tessa.Cards.CardTypeTabForm] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitValidatorAsync(CardTypeValidator, CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitValidatorAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
[VisitValidatorAsync(CardTypeValidator, CardTypeCompletionOption, CardType,
CancellationToken)](M_Tessa_Cards_CardTypeVisitor_VisitValidatorAsync_1.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки для варианта
завершения.  
(Унаследован от [CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm))  
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
