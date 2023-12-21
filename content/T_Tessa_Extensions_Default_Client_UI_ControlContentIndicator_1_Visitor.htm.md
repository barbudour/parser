# ControlContentIndicator<T>.Visitor - класс
Выполняет обход дерева элементов управления в ширину. При выполнении обхода
составляется массив содержащий связи между элементами управления и физическими
полями.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI](N_Tessa_Extensions_Default_Client_UI.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     protected sealed class Visitor : BreadthFirstControlVisitor
VB __Копировать
     Protected NotInheritable Class Visitor
    	Inherits BreadthFirstControlVisitor
C++ __Копировать
     protected ref class Visitor sealed : public BreadthFirstControlVisitor
F# __Копировать
     [<SealedAttribute>]
    type Visitor = 
        class
            inherit BreadthFirstControlVisitor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[BreadthFirstControlVisitor](T_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor.htm) __ ControlContentIndicator<T>.Visitor
##  __Конструкторы
[ControlContentIndicator<T>.Visitor](M_Tessa_Extensions_Default_Client_UI_ControlContentIndicator_1_Visitor__ctor.htm)|
Инициализирует новый экземпляр класса ControlContentIndicator<T>.Visitor.  
---|---  
## __Свойства
[Index](P_Tessa_Extensions_Default_Client_UI_ControlContentIndicator_1_Visitor_Index.htm)|
Возвращает или задаёт порядковый номер элемента управления к которому
относится поле.  
---|---  
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
[Visit(IBlockViewModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_Visit.htm)|  
(Унаследован от
[BreadthFirstControlVisitor](T_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor.htm))  
[Visit(ICardModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_Visit_1.htm)|  
(Унаследован от
[BreadthFirstControlVisitor](T_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor.htm))  
[Visit(IControlViewModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_Visit_2.htm)|  
(Унаследован от
[BreadthFirstControlVisitor](T_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor.htm))  
[Visit(IFormViewModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_Visit_3.htm)|  
(Унаследован от
[BreadthFirstControlVisitor](T_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor.htm))  
[VisitBlock](M_Tessa_Extensions_Default_Client_UI_ControlContentIndicator_1_Visitor_VisitBlock.htm)|  
(Переопределяет
[BreadthFirstControlVisitor.VisitBlock(IBlockViewModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_VisitBlock.htm))  
[VisitControl](M_Tessa_Extensions_Default_Client_UI_ControlContentIndicator_1_Visitor_VisitControl.htm)|  
(Переопределяет
[BreadthFirstControlVisitor.VisitControl(IControlViewModel)](M_Tessa_Extensions_Default_Client_UI_BreadthFirstControlVisitor_VisitControl.htm))  
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
[Tessa.Extensions.Default.Client.UI - пространство
имён](N_Tessa_Extensions_Default_Client_UI.htm)
