# SmartMergerBase<TMergeObject, TMergeOptions> \- класс
Абстрактный базовый класс для типичной реализации мерджера через
IMergeTreeBuilder и IMergeMetadataBuilder
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SmartMergerBase<TMergeObject, TMergeOptions> : ISmartMerger<TMergeObject>
    where TMergeOptions : IMergeOptions
VB __Копировать
     Public MustInherit Class SmartMergerBase(Of TMergeObject, TMergeOptions As IMergeOptions)
    	Implements ISmartMerger(Of TMergeObject)
C++ __Копировать
    generic<typename TMergeObject, typename TMergeOptions>
    where TMergeOptions : IMergeOptions
    public ref class SmartMergerBase abstract : ISmartMerger<TMergeObject>
F# __Копировать
     [<AbstractClassAttribute>]
    type SmartMergerBase<'TMergeObject, 'TMergeOptions when 'TMergeOptions : IMergeOptions> = 
        class
            interface ISmartMerger<'TMergeObject>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SmartMergerBase<TMergeObject, TMergeOptions>
Derived
[Tessa.Cards.SmartMerge.CardSmartMerger](T_Tessa_Cards_SmartMerge_CardSmartMerger.htm)
Implements
    [ISmartMerger](T_Tessa_SmartMerge_ISmartMerger_1.htm)<TMergeObject>
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние
TMergeOptions
    Тип опций слияния
##  __Конструкторы
[SmartMergerBase<TMergeObject,
TMergeOptions>](M_Tessa_SmartMerge_SmartMergerBase_2__ctor.htm)|
Инициализирует новый экземпляр класса SmartMergerBase<TMergeObject,
TMergeOptions>  
---|---  
##  __Свойства
[MergeMetadataBuilder](P_Tessa_SmartMerge_SmartMergerBase_2_MergeMetadataBuilder.htm)|  
---|---  
[MergeTreeBuilder](P_Tessa_SmartMerge_SmartMergerBase_2_MergeTreeBuilder.htm)|  
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
[MergeAsync](M_Tessa_SmartMerge_SmartMergerBase_2_MergeAsync.htm)|  
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
