# INumberDependencies - интерфейс
Объект, содержащий внешние зависимости API номеров, которые обычно требуются
для построения таких объектов, как
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm) и
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm). Каждый экземпляр
создаваемого из Unity объекта должен получить свой экземпляр объекта с
зависимостями.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberDependencies
VB __Копировать
     Public Interface INumberDependencies
C++ __Копировать
     public interface class INumberDependencies
F# __Копировать
     type INumberDependencies = interface end
##  __Свойства
[DbScope](P_Tessa_Cards_Numbers_INumberDependencies_DbScope.htm)|  Объект,
предоставляющий доступ к базе данных, или null, если выполнение происходит без
доступа к базе данных, например, со стороны клиента.  
---|---  
[PlaceholderManager](P_Tessa_Cards_Numbers_INumberDependencies_PlaceholderManager.htm)|
Объект, управляющий операциями с плейсхолдерами.  
[RequestRepository](P_Tessa_Cards_Numbers_INumberDependencies_RequestRepository.htm)|
Репозиторий, используемый для построения универсальных запросов к API номеров
на сервере.  
[Session](P_Tessa_Cards_Numbers_INumberDependencies_Session.htm)| Сессия
текущего пользователя.  
[UnityContainer](P_Tessa_Cards_Numbers_INumberDependencies_UnityContainer.htm)|
Контейнер Unity, который может использоваться для получения дополнительных
зависимостей.  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
