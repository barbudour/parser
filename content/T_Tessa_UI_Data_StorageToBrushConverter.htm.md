# StorageToBrushConverter - класс
Преобразует значения [StorageColor](T_Tessa_Platform_Storage_StorageColor.htm)
или
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm)
в соответствующую кисть
[SolidColorBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.solidcolorbrush)
или
[LinearGradientBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.lineargradientbrush).
## __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class StorageToBrushConverter : ValueConverter<Object, Brush>
VB __Копировать
     Public Class StorageToBrushConverter
    	Inherits ValueConverter(Of Object, Brush)
C++ __Копировать
     public ref class StorageToBrushConverter : public ValueConverter<Object^, Brush^>
F# __Копировать
     type StorageToBrushConverter = 
        class
            inherit ValueConverter<Object, Brush>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueConverter](T_Tessa_UI_Data_ValueConverter_2.htm)<[Object](https://learn.microsoft.com/dotnet/api/system.object), [Brush](https://learn.microsoft.com/dotnet/api/system.windows.media.brush)> __ StorageToBrushConverter
##  __Конструкторы
[StorageToBrushConverter](M_Tessa_UI_Data_StorageToBrushConverter__ctor.htm)|
Инициализирует новый экземпляр класса StorageToBrushConverter  
---|---  
##  __Свойства
[FreezeBrush](P_Tessa_UI_Data_StorageToBrushConverter_FreezeBrush.htm)|  
---|---  
[Instance](P_Tessa_UI_Data_StorageToBrushConverter_Instance.htm)|  
[InstanceWithFreeze](P_Tessa_UI_Data_StorageToBrushConverter_InstanceWithFreeze.htm)|  
## __Методы
[BoxSourceValue](M_Tessa_UI_Data_ValueConverter_2_BoxSourceValue.htm)|  
(Унаследован от [ValueConverter<TSource,
TTarget>](T_Tessa_UI_Data_ValueConverter_2.htm))  
---|---  
[BoxTargetValue](M_Tessa_UI_Data_ValueConverter_2_BoxTargetValue.htm)|  
(Унаследован от [ValueConverter<TSource,
TTarget>](T_Tessa_UI_Data_ValueConverter_2.htm))  
[Convert(Object, Object,
CultureInfo)](M_Tessa_UI_Data_StorageToBrushConverter_Convert.htm)|  
(Переопределяет [ValueConverter<TSource, TTarget>.Convert(TSource, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_Convert_1.htm))  
[Convert(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_Convert.htm)|  
(Унаследован от [ValueConverter<TSource,
TTarget>](T_Tessa_UI_Data_ValueConverter_2.htm))  
[ConvertBack(Brush, Object,
CultureInfo)](M_Tessa_UI_Data_StorageToBrushConverter_ConvertBack.htm)|  
(Переопределяет [ValueConverter<TSource, TTarget>.ConvertBack(TTarget, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_ConvertBack_1.htm))  
[ConvertBack(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_ConvertBack.htm)|  
(Унаследован от [ValueConverter<TSource,
TTarget>](T_Tessa_UI_Data_ValueConverter_2.htm))  
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
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
