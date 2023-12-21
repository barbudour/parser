# IProcessNameResolver - интерфейс
Объект, обеспечивающий получение отображаемого имени приложения по
запускающему файлу процесса, обычно по .exe.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IProcessNameResolver
VB __Копировать
     Public Interface IProcessNameResolver
C++ __Копировать
     public interface class IProcessNameResolver
F# __Копировать
     type IProcessNameResolver = interface end
##  __Методы
[Contains](M_Tessa_Platform_IProcessNameResolver_Contains.htm)|  Возвращает
признак того, что текущий объект содержит информацию по имени приложения для
заданного имени файла, запускающего приложение.  
---|---  
[Register](M_Tessa_Platform_IProcessNameResolver_Register.htm)|  Выполняет
регистрацию имени приложения, пригодного для отображения пользователю, по
имени файла, запускающего приложение.  
[Remove](M_Tessa_Platform_IProcessNameResolver_Remove.htm)| Удаляет информацию
по имени приложения для заданного имени файла, запускающего приложение.  
[Resolve](M_Tessa_Platform_IProcessNameResolver_Resolve.htm)|  Возвращает имя
приложения, пригодное для отображению пользователю. Если подходящего имени не
было найдено, то возвращает значение параметра executableName.  
## __Методы расширения
[Resolve](M_Tessa_Platform_PlatformExtensions_Resolve.htm)|  Возвращает имя
процесса, пригодное для отображения пользователю.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
