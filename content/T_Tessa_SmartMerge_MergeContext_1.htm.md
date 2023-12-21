# MergeContext<TMergeOptions> \- класс
Реализует контекст слияния.
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class MergeContext<TMergeOptions> : IMergeContext<TMergeOptions>
    where TMergeOptions : new(), IMergeOptions
VB __Копировать
     Public Class MergeContext(Of TMergeOptions As {New, IMergeOptions})
    	Implements IMergeContext(Of TMergeOptions)
C++ __Копировать
    generic<typename TMergeOptions>
    where TMergeOptions : gcnew(), IMergeOptions
    public ref class MergeContext : IMergeContext<TMergeOptions>
F# __Копировать
     type MergeContext<'TMergeOptions when 'TMergeOptions : new() and IMergeOptions> = 
        class
            interface IMergeContext<'TMergeOptions>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MergeContext<TMergeOptions>
Implements
    [IMergeContext](T_Tessa_SmartMerge_IMergeContext_1.htm)<TMergeOptions>
#### Параметры типа
TMergeOptions
    Тип опций слияния
##  __Конструкторы
[MergeContext<TMergeOptions>()](M_Tessa_SmartMerge_MergeContext_1__ctor.htm)|
Инициализирует новый экземпляр класса MergeContext<TMergeOptions>  
---|---  
[MergeContext<TMergeOptions>(IValidationResultBuilder, Object, TMergeOptions,
ILogger, Int32)](M_Tessa_SmartMerge_MergeContext_1__ctor_1.htm)|
Инициализирует новый экземпляр класса MergeContext<TMergeOptions>  
##  __Свойства
[ComparisonLevels](P_Tessa_SmartMerge_MergeContext_1_ComparisonLevels.htm)|
Количество уровней сравнения для текущего случая слияния.  
---|---  
[Logger](P_Tessa_SmartMerge_MergeContext_1_Logger.htm)|  
[MergeObject](P_Tessa_SmartMerge_MergeContext_1_MergeObject.htm)|  Объект
слияния.  
[MergeOptions](P_Tessa_SmartMerge_MergeContext_1_MergeOptions.htm)|  Опции
слияния  
[ValidationResult](P_Tessa_SmartMerge_MergeContext_1_ValidationResult.htm)|
Результат валидации.  
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
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
