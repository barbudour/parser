# TileAreaWidthConverter - класс
Конвертер, преобразующий высоту боковой панели в ширину области с верхнего и
нижнего краёв экрана, по которой можно открыть боковую панель.
## __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
    [ValueConversionAttribute(typeof(double), typeof(double))]
    public sealed class TileAreaWidthConverter : IValueConverter
VB __Копировать
    <ValueConversionAttribute(GetType(Double), GetType(Double))>
    Public NotInheritable Class TileAreaWidthConverter
    	Implements IValueConverter
C++ __Копировать
    [ValueConversionAttribute(typeof(double), typeof(double))]
    public ref class TileAreaWidthConverter sealed : IValueConverter
F# __Копировать
     [<SealedAttribute>]
    [<ValueConversionAttribute(typeof(float), typeof(float))>]
    type TileAreaWidthConverter = 
        class
            interface IValueConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TileAreaWidthConverter
Implements
    [IValueConverter](https://learn.microsoft.com/dotnet/api/system.windows.data.ivalueconverter)
##  __Конструкторы
[TileAreaWidthConverter](M_Tessa_UI_Data_TileAreaWidthConverter__ctor.htm)|
Инициализирует новый экземпляр класса TileAreaWidthConverter  
---|---  
##  __Методы
[Convert](M_Tessa_UI_Data_TileAreaWidthConverter_Convert.htm)| Выполняет
прямое преобразование заданного значения.  
---|---  
[ConvertBack](M_Tessa_UI_Data_TileAreaWidthConverter_ConvertBack.htm)|
Выполняет обратное преобразование заданного значения.  
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
##  __Поля
[HeightToWidthMultiplier](F_Tessa_UI_Data_TileAreaWidthConverter_HeightToWidthMultiplier.htm)|
Множитель, преобразующий высоту боковой панели в ширину области с верхнего и
нижнего краёв экрана, по которой можно открыть боковую панель.  
---|---  
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
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
