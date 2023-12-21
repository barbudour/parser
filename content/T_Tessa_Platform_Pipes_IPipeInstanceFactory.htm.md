# IPipeInstanceFactory - интерфейс
Фабрика экземпляров объектов, используемых в канале, время жизни которых
контролируется объектом
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeInstanceFactory
VB __Копировать
     Public Interface IPipeInstanceFactory
C++ __Копировать
     public interface class IPipeInstanceFactory
F# __Копировать
     type IPipeInstanceFactory = interface end
##  __Методы
[CreateInstanceAsync](M_Tessa_Platform_Pipes_IPipeInstanceFactory_CreateInstanceAsync.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу type и не равен null.  
---|---  
[Register](M_Tessa_Platform_Pipes_IPipeInstanceFactory_Register.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу type.  
## __Методы расширения
[CreateInstanceAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_CreateInstanceAsync__1.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу T и не равен null.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу T.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
