# CardWithoutLockingStrategy - класс
Стратегия по управлению блокировками на чтение и запись карточек, которая не
выполняет взятие блокировок. Некорректное использование методов в этом
интерфейсе может привести к "повисшим" блокировкам, используйте с
осторожностью.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardWithoutLockingStrategy : ICardLockingStrategy
VB __Копировать
     Public Class CardWithoutLockingStrategy
    	Implements ICardLockingStrategy
C++ __Копировать
     public ref class CardWithoutLockingStrategy : ICardLockingStrategy
F# __Копировать
     type CardWithoutLockingStrategy = 
        class
            interface ICardLockingStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardWithoutLockingStrategy
Implements
    [ICardLockingStrategy](T_Tessa_Cards_ICardLockingStrategy.htm)
##  __Заметки
Наследники класса могут определять дополнительные свойства и методы, а также
переопределять существующие методы.
## __Конструкторы
[CardWithoutLockingStrategy](M_Tessa_Cards_CardWithoutLockingStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[ConfigurationInfoProvider](P_Tessa_Cards_CardWithoutLockingStrategy_ConfigurationInfoProvider.htm)|
Провайдер информации о конфигурации.  
---|---  
[DbScope](P_Tessa_Cards_CardWithoutLockingStrategy_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных.  
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
[ObtainReaderLockAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ObtainReaderLockAsync.htm)|
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.  
[ObtainReaderLockCoreAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ObtainReaderLockCoreAsync.htm)|
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.  
[ObtainWriterLockAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ObtainWriterLockAsync.htm)|
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.  
[ObtainWriterLockCoreAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ObtainWriterLockCoreAsync.htm)|
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.  
[ReleaseReaderLockAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ReleaseReaderLockAsync.htm)|
Выполняет снятие блокировки на чтение карточки.  
[ReleaseReaderLockCoreAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ReleaseReaderLockCoreAsync.htm)|
Выполняет снятие блокировки на чтение карточки.  
[ReleaseWriterLockAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ReleaseWriterLockAsync.htm)|
Выполняет снятие блокировки на запись карточки.  
[ReleaseWriterLockCoreAsync](M_Tessa_Cards_CardWithoutLockingStrategy_ReleaseWriterLockCoreAsync.htm)|
Выполняет снятие блокировки на запись карточки.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
