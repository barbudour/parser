# ISplash - интерфейс
Объект, предоставляющий доступ к окну с экраном загрузки.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISplash : IDisposable
VB __Копировать
     Public Interface ISplash
    	Inherits IDisposable
C++ __Копировать
     public interface class ISplash : IDisposable
F# __Копировать
     type ISplash = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[IsCollapsed](P_Tessa_Platform_ISplash_IsCollapsed.htm)|  Признак того, что
всплывающее окно скрыто. Посредством этого свойства можно временно скрыть
окно. Если окно ещё не отображеноб то всегда возвращает false, а если уже
освобождено, то возвращает значение true и не вызывает исключений. Установка
значения в таких случаях не вызывает действий.  
---|---  
[Text](P_Tessa_Platform_ISplash_Text.htm)| Текст, отображаемый в окне
операции.  
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
