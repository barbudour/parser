# CardCacheProxy - класс
Прокси для потокобезопасного кэша с карточками и дополнительными настройками.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardCacheProxy : ICardCache
VB __Копировать
     Public Class CardCacheProxy
    	Implements ICardCache
C++ __Копировать
     public ref class CardCacheProxy : ICardCache
F# __Копировать
     type CardCacheProxy = 
        class
            interface ICardCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardCacheProxy
Implements
    [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
##  __Конструкторы
[CardCacheProxy](M_Tessa_Cards_Caching_CardCacheProxy__ctor.htm)|  Создаёт
экземпляр класса с указанием декорируемого объекта и метода, выполняемого при
очистке кэша вызовом метода интерфейса
[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm).  
---|---  
## __Свойства
[Cards](P_Tessa_Cards_Caching_CardCacheProxy_Cards.htm)| Кэш карточек,
доступных по строковому ключу.  
---|---  
[Settings](P_Tessa_Cards_Caching_CardCacheProxy_Settings.htm)| Кэш настроек,
доступных по строковому ключу и функции заполнения значения, отсутствующего в
кэше.  
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
[InvalidateAsync](M_Tessa_Cards_Caching_CardCacheProxy_InvalidateAsync.htm)|
Сбрасывает локальный кэш.  
[InvalidateSourceAsync](M_Tessa_Cards_Caching_CardCacheProxy_InvalidateSourceAsync.htm)|
Сбрасывает локальный кэш.  
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
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
