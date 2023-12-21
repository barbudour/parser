# CardGetGlobalCachingStrategy - класс
Стратегия кэширования объектов для операции по загрузке карточки с
использованием глобального кэша с метаинформацией карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardGetGlobalCachingStrategy : ICardGetCachingStrategy
VB __Копировать
     Public NotInheritable Class CardGetGlobalCachingStrategy
    	Implements ICardGetCachingStrategy
C++ __Копировать
     public ref class CardGetGlobalCachingStrategy sealed : ICardGetCachingStrategy
F# __Копировать
     [<SealedAttribute>]
    type CardGetGlobalCachingStrategy = 
        class
            interface ICardGetCachingStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetGlobalCachingStrategy
Implements
    [ICardGetCachingStrategy](T_Tessa_Cards_ComponentModel_ICardGetCachingStrategy.htm)
##  __Заметки
Очистка глобального кэша может быть инициирована между различными процессами,
осуществляющими хостинг сервиса карточек.
## __Конструкторы
[CardGetGlobalCachingStrategy](M_Tessa_Cards_ComponentModel_CardGetGlobalCachingStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[AddLoader](M_Tessa_Cards_ComponentModel_CardGetGlobalCachingStrategy_AddLoader.htm)|
Добавляет в кэш объект, выполняющий загрузку данных карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.  
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
[TryGetLoader](M_Tessa_Cards_ComponentModel_CardGetGlobalCachingStrategy_TryGetLoader.htm)|
Возвращает из кэша объект, выполняющий загрузку данных карточки заданного
типа, или null, если объект не найден в кэше.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
