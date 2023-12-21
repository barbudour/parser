# ConcurrentKeyCache<T> \- класс
Кэш, осуществляющий перевод строго типизированных ключей в строки и наоборот.
К кэшу возможен неблокирующий доступ из нескольких потоков.
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ConcurrentKeyCache<T> : IKeyCache<T>
VB __Копировать
     Public Class ConcurrentKeyCache(Of T)
    	Implements IKeyCache(Of T)
C++ __Копировать
    generic<typename T>
    public ref class ConcurrentKeyCache : IKeyCache<T>
F# __Копировать
     type ConcurrentKeyCache<'T> = 
        class
            interface IKeyCache<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConcurrentKeyCache<T>
Implements
    [IKeyCache](T_Tessa_Platform_Caching_IKeyCache_1.htm)<T>
#### Параметры типа
T
    Тип строго типизированного ключа.
##  __Конструкторы
[ConcurrentKeyCache<T>](M_Tessa_Platform_Caching_ConcurrentKeyCache_1__ctor.htm)|
Создаёт экземпляр класса с указанием максимального количества записей в кэше.  
---|---  
## __Свойства
[Capacity](P_Tessa_Platform_Caching_ConcurrentKeyCache_1_Capacity.htm)|
Максимальное количество записей в кэше или 0, если количество записей не
ограничено.  
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
[GetStringKey](M_Tessa_Platform_Caching_ConcurrentKeyCache_1_GetStringKey.htm)|
Возвращает строковый ключ по строго типизированному с указанием функции
преобразования ключей.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetTypedKey](M_Tessa_Platform_Caching_ConcurrentKeyCache_1_GetTypedKey.htm)|
Возвращает строго типизированный ключ по строковому с указанием функции
преобразования ключей.  
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
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
