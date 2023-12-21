# CardLockingStrategy - класс
Стратегия по управлению блокировками на чтение и запись карточек. Некорректное
использование методов в этом интерфейсе может привести к "повисшим"
блокировкам, используйте с осторожностью.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardLockingStrategy : ICardLockingStrategy
VB __Копировать
     Public Class CardLockingStrategy
    	Implements ICardLockingStrategy
C++ __Копировать
     public ref class CardLockingStrategy : ICardLockingStrategy
F# __Копировать
     type CardLockingStrategy = 
        class
            interface ICardLockingStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardLockingStrategy
Implements
    [ICardLockingStrategy](T_Tessa_Cards_ICardLockingStrategy.htm)
##  __Заметки
Наследники класса могут определять дополнительные свойства и методы, а также
переопределять существующие методы.
## __Конструкторы
[CardLockingStrategy](M_Tessa_Cards_CardLockingStrategy__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[ConfigurationInfoProvider](P_Tessa_Cards_CardLockingStrategy_ConfigurationInfoProvider.htm)|
Провайдер информации о конфигурации.  
---|---  
[DbScope](P_Tessa_Cards_CardLockingStrategy_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных.  
[ObtainLockCommandTimeoutSeconds](P_Tessa_Cards_CardLockingStrategy_ObtainLockCommandTimeoutSeconds.htm)|
Таймаут на выполнение команд взятия блокировок в секундах. При таком таймауте
блокировка может быть взята в БД, но не взята с точки зрения сервера .NET.
Берём 15 минут, а не бесконечность, на случай, когда сервер СУБД безвозвратно
упал.  
[ReleaseLockCommandTimeoutSeconds](P_Tessa_Cards_CardLockingStrategy_ReleaseLockCommandTimeoutSeconds.htm)|
Таймаут на снятие блокировок в секундах. Берём 5 минут, а не бесконечность, на
случай, когда сервер СУБД безвозвратно упал.  
[Session](P_Tessa_Cards_CardLockingStrategy_Session.htm)|  Сессия для текущего
пользователя.  
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
[ObtainReaderLockAsync](M_Tessa_Cards_CardLockingStrategy_ObtainReaderLockAsync.htm)|
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.  
[ObtainReaderLockCoreAsync](M_Tessa_Cards_CardLockingStrategy_ObtainReaderLockCoreAsync.htm)|
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.  
[ObtainWriterLockAsync](M_Tessa_Cards_CardLockingStrategy_ObtainWriterLockAsync.htm)|
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.  
[ObtainWriterLockCoreAsync](M_Tessa_Cards_CardLockingStrategy_ObtainWriterLockCoreAsync.htm)|
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.  
[ReleaseReaderLockAsync](M_Tessa_Cards_CardLockingStrategy_ReleaseReaderLockAsync.htm)|
Выполняет снятие блокировки на чтение карточки.  
[ReleaseReaderLockCoreAsync](M_Tessa_Cards_CardLockingStrategy_ReleaseReaderLockCoreAsync.htm)|
Выполняет снятие блокировки на чтение карточки.  
[ReleaseWriterLockAsync](M_Tessa_Cards_CardLockingStrategy_ReleaseWriterLockAsync.htm)|
Выполняет снятие блокировки на запись карточки.  
[ReleaseWriterLockCoreAsync](M_Tessa_Cards_CardLockingStrategy_ReleaseWriterLockCoreAsync.htm)|
Выполняет снятие блокировки на запись карточки.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CardNotFoundWhileWritingCode](F_Tessa_Cards_CardLockingStrategy_CardNotFoundWhileWritingCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если
карточка не существует.  
---|---  
[LockedByReadersCode](F_Tessa_Cards_CardLockingStrategy_LockedByReadersCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
не дождался окончания чтения другими reader'ами.  
[LockedByWriterCode](F_Tessa_Cards_CardLockingStrategy_LockedByWriterCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock или ObtainReaderLock
в случае, если writer не дождался снятия блокировки другим writer'ом.  
[LockedWithChangedVersion](F_Tessa_Cards_CardLockingStrategy_LockedWithChangedVersion.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
не дождался снятия блокировки другим writer'ом. ///  
[LockObtained](F_Tessa_Cards_CardLockingStrategy_LockObtained.htm)|  Результат
выполнения хранимой процедуры ObtainWriterLock или ObtainReaderLock в случае,
если блокировка успешно получена.  
[LockTimeoutWhileObtainingWriterLockCode](F_Tessa_Cards_CardLockingStrategy_LockTimeoutWhileObtainingWriterLockCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
натолкнулся на длительную блокировку Instances в процессе выполнения запроса и
не дождался снятия блокировки другим writer'ом.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
