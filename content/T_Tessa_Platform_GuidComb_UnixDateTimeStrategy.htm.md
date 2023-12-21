# UnixDateTimeStrategy - класс
This strategy stores the Unix epoch timestamp, scaled to milliseconds, in 48
unsigned bits. The allowed date range is 1970-01-01 to 8419-05-26.
## __Definition
 **Пространство имён:**
[Tessa.Platform.GuidComb](N_Tessa_Platform_GuidComb.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class UnixDateTimeStrategy : IGuidCombDateTimeStrategy
VB __Копировать
     Public Class UnixDateTimeStrategy
    	Implements IGuidCombDateTimeStrategy
C++ __Копировать
     public ref class UnixDateTimeStrategy : IGuidCombDateTimeStrategy
F# __Копировать
     type UnixDateTimeStrategy = 
        class
            interface IGuidCombDateTimeStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UnixDateTimeStrategy
Implements
    [IGuidCombDateTimeStrategy](T_Tessa_Platform_GuidComb_IGuidCombDateTimeStrategy.htm)
##  __Конструкторы
[UnixDateTimeStrategy](M_Tessa_Platform_GuidComb_UnixDateTimeStrategy__ctor.htm)|
Инициализирует новый экземпляр класса UnixDateTimeStrategy  
---|---  
##  __Свойства
[MaxDateTimeValue](P_Tessa_Platform_GuidComb_UnixDateTimeStrategy_MaxDateTimeValue.htm)|  
---|---  
[MinDateTimeValue](P_Tessa_Platform_GuidComb_UnixDateTimeStrategy_MinDateTimeValue.htm)|  
[NumDateBytes](P_Tessa_Platform_GuidComb_UnixDateTimeStrategy_NumDateBytes.htm)|  
## __Методы
[BytesToDateTime](M_Tessa_Platform_GuidComb_UnixDateTimeStrategy_BytesToDateTime.htm)|  
---|---  
[DateTimeToBytes](M_Tessa_Platform_GuidComb_UnixDateTimeStrategy_DateTimeToBytes.htm)|  
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
[FromUnixTimeMilliseconds](M_Tessa_Platform_GuidComb_UnixDateTimeStrategy_FromUnixTimeMilliseconds.htm)|  
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
[ToUnixTimeMilliseconds](M_Tessa_Platform_GuidComb_UnixDateTimeStrategy_ToUnixTimeMilliseconds.htm)|  
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
[Tessa.Platform.GuidComb - пространство имён](N_Tessa_Platform_GuidComb.htm)
