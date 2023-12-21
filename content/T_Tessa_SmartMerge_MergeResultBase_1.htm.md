# MergeResultBase<TMergeObject> \- класс
Базовый класс для реализации результатов слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class MergeResultBase<TMergeObject> : IMergeResult<TMergeObject>
VB __Копировать
     Public MustInherit Class MergeResultBase(Of TMergeObject)
    	Implements IMergeResult(Of TMergeObject)
C++ __Копировать
    generic<typename TMergeObject>
    public ref class MergeResultBase abstract : IMergeResult<TMergeObject>
F# __Копировать
     [<AbstractClassAttribute>]
    type MergeResultBase<'TMergeObject> = 
        class
            interface IMergeResult<'TMergeObject>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MergeResultBase<TMergeObject>
Derived
[Tessa.Cards.SmartMerge.CardMergeResult](T_Tessa_Cards_SmartMerge_CardMergeResult.htm)
Implements
    [IMergeResult](T_Tessa_SmartMerge_IMergeResult_1.htm)<TMergeObject>
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
##  __Конструкторы
[MergeResultBase<TMergeObject>](M_Tessa_SmartMerge_MergeResultBase_1__ctor.htm)|
Инициализирует новый экземпляр класса MergeResultBase<TMergeObject>  
---|---  
##  __Свойства
[MergeResultItems](P_Tessa_SmartMerge_MergeResultBase_1_MergeResultItems.htm)|
Список результатов слияния.  
---|---  
[ValidationResult](P_Tessa_SmartMerge_MergeResultBase_1_ValidationResult.htm)|
Результат валидации.  
## __Методы
[ApplyAsync](M_Tessa_SmartMerge_MergeResultBase_1_ApplyAsync.htm)|  Применяет
результат слияния к объекту слияния.  
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
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
