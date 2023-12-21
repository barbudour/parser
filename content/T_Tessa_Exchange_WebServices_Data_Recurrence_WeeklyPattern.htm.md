# Recurrence.WeeklyPattern - класс
Represents a recurrence pattern where each occurrence happens on specific days
a specific number of weeks after the previous one.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WeeklyPattern : Recurrence.IntervalPattern
VB __Копировать
     Public NotInheritable Class WeeklyPattern
    	Inherits Recurrence.IntervalPattern
C++ __Копировать
     public ref class WeeklyPattern sealed : public Recurrence.IntervalPattern
F# __Копировать
     [<SealedAttribute>]
    type WeeklyPattern = 
        class
            inherit Recurrence.IntervalPattern
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm) __[Recurrence.IntervalPattern](T_Tessa_Exchange_WebServices_Data_Recurrence_IntervalPattern.htm) __ Recurrence.WeeklyPattern
##  __Конструкторы
[Recurrence.WeeklyPattern()](M_Tessa_Exchange_WebServices_Data_Recurrence_WeeklyPattern__ctor.htm)|
Initializes a new instance of the Recurrence.WeeklyPattern class.  
---|---  
[Recurrence.WeeklyPattern(DateTime, Int32,
DayOfTheWeek[])](M_Tessa_Exchange_WebServices_Data_Recurrence_WeeklyPattern__ctor_1.htm)|
Initializes a new instance of the Recurrence.WeeklyPattern class.  
## __Свойства
[DaysOfTheWeek](P_Tessa_Exchange_WebServices_Data_Recurrence_WeeklyPattern_DaysOfTheWeek.htm)|
Gets the list of the days of the week when occurrences happen.  
---|---  
[EndDate](P_Tessa_Exchange_WebServices_Data_Recurrence_EndDate.htm)|  Gets or
sets the date after which the recurrence ends. Setting EndDate resets
NumberOfOccurrences.  
(Унаследован от
[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm))  
[FirstDayOfWeek](P_Tessa_Exchange_WebServices_Data_Recurrence_WeeklyPattern_FirstDayOfWeek.htm)|
Gets or sets the first day of the week for this recurrence.  
[HasEnd](P_Tessa_Exchange_WebServices_Data_Recurrence_HasEnd.htm)|  Gets a
value indicating whether the pattern has a fixed number of occurrences or an
end date.  
(Унаследован от
[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm))  
[Interval](P_Tessa_Exchange_WebServices_Data_Recurrence_IntervalPattern_Interval.htm)|
Gets or sets the interval between occurrences.  
(Унаследован от
[Recurrence.IntervalPattern](T_Tessa_Exchange_WebServices_Data_Recurrence_IntervalPattern.htm))  
[NumberOfOccurrences](P_Tessa_Exchange_WebServices_Data_Recurrence_NumberOfOccurrences.htm)|
Gets or sets the number of occurrences after which the recurrence ends.
Setting NumberOfOccurrences resets EndDate.  
(Унаследован от
[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm))  
[StartDate](P_Tessa_Exchange_WebServices_Data_Recurrence_StartDate.htm)|  Gets
or sets the date and time when the recurrence start.  
(Унаследован от
[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm))  
##  __Методы
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
[IsSame](M_Tessa_Exchange_WebServices_Data_Recurrence_WeeklyPattern_IsSame.htm)|
Checks if two recurrence objects are identical.  
(Переопределяет
[Recurrence.IntervalPattern.IsSame(Recurrence)](M_Tessa_Exchange_WebServices_Data_Recurrence_IntervalPattern_IsSame.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NeverEnds](M_Tessa_Exchange_WebServices_Data_Recurrence_NeverEnds.htm)|  Sets
up this recurrence so that it never ends. Calling NeverEnds is equivalent to
setting both NumberOfOccurrences and EndDate to null.  
(Унаследован от
[Recurrence](T_Tessa_Exchange_WebServices_Data_Recurrence.htm))  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
