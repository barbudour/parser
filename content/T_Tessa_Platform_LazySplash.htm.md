# LazySplash - класс
Объект, предоставляющий доступ к окну с экраном загрузки, который создаётся
отложенно при изменении свойства [Text](P_Tessa_Platform_ISplash_Text.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LazySplash : ISplash, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class LazySplash
    	Implements ISplash, IDisposable
C++ __Копировать
     public ref class LazySplash sealed : ISplash, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type LazySplash = 
        class
            interface ISplash
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LazySplash
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISplash](T_Tessa_Platform_ISplash.htm)
##  __Конструкторы
[LazySplash](M_Tessa_Platform_LazySplash__ctor.htm)|  Создаёт экземпляр класса
с указанием объекта, создающего основную операцию по требованию.  
---|---  
## __Свойства
[IsCollapsed](P_Tessa_Platform_LazySplash_IsCollapsed.htm)|  Признак того, что
всплывающее окно скрыто. Посредством этого свойства можно временно скрыть
окно. Если окно ещё не отображеноб то всегда возвращает false, а если уже
освобождено, то возвращает значение true и не вызывает исключений. Установка
значения в таких случаях не вызывает действий.  
---|---  
[Text](P_Tessa_Platform_LazySplash_Text.htm)| Текст, отображаемый в окне
операции.  
##  __Методы
[Dispose](M_Tessa_Platform_LazySplash_Dispose.htm)|  Закрывает окно с экраном
загрузки.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
