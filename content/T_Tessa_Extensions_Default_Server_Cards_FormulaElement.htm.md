# FormulaElement - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FormulaElement : WorksheetBase<CellFormula>
VB __Копировать
     Public NotInheritable Class FormulaElement
    	Inherits WorksheetBase(Of CellFormula)
C++ __Копировать
     public ref class FormulaElement sealed : public WorksheetBase<CellFormula^>
F# __Копировать
     [<SealedAttribute>]
    type FormulaElement = 
        class
            inherit WorksheetBase<CellFormula>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<CellFormula> __[WorksheetBase](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)<CellFormula> __ FormulaElement
##  __Конструкторы
[FormulaElement](M_Tessa_Extensions_Default_Server_Cards_FormulaElement__ctor.htm)|
Инициализирует новый экземпляр класса FormulaElement  
---|---  
##  __Свойства
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
---|---  
[FormulaSources](P_Tessa_Extensions_Default_Server_Cards_FormulaElement_FormulaSources.htm)|  
[OriginalFormula](P_Tessa_Extensions_Default_Server_Cards_FormulaElement_OriginalFormula.htm)|  
[Reference](P_Tessa_Extensions_Default_Server_Cards_FormulaElement_Reference.htm)|  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1_Worksheet.htm)|
Объект Worksheet, на базе которого хранится текущий объект  
(Унаследован от
[WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm))  
##  __Методы
[Clone](M_Tessa_Extensions_Default_Server_Cards_FormulaElement_Clone.htm)|
Метод не предусмотрен для формул  
(Переопределяет
[ElementBase<TElement>.Clone()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Clone.htm))  
---|---  
[CloneElement](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_CloneElement.htm)|
Метод для клонирования хранимого элемента  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
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
[Insert](M_Tessa_Extensions_Default_Server_Cards_FormulaElement_Insert.htm)|
Метод не предусмотрен для формул  
(Переопределяет
[ElementBase<TElement>.Insert()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Insert.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_FormulaElement_ParseElement.htm)|  
(Переопределяет
[ElementBase<TElement>.ParseElement()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm))  
[Remove](M_Tessa_Extensions_Default_Server_Cards_FormulaElement_Remove.htm)|
Удаляем текст ячейки вместе с формулой, где она находится.  
(Переопределяет
[ElementBase<TElement>.Remove()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_FormulaElement_Update.htm)|  
(Переопределяет
[ElementBase<TElement>.Update()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Update.htm))  
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
[Tessa.Extensions.Default.Server.Cards - пространство
имён](N_Tessa_Extensions_Default_Server_Cards.htm)
