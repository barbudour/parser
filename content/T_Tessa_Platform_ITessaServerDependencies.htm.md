# ITessaServerDependencies - интерфейс
Зависимости платформы, которые зависят от разновидности сервера приложений, и
определяет возможности такого сервера, требующие дополнительные зависимости.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaServerDependencies
VB __Копировать
     Public Interface ITessaServerDependencies
C++ __Копировать
     public interface class ITessaServerDependencies
F# __Копировать
     type ITessaServerDependencies = interface end
##  __Методы
[FinalizeServerRegistration](M_Tessa_Platform_ITessaServerDependencies_FinalizeServerRegistration.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
завершения регистрации, вызываемого на сервере. Метод вызывается после того,
как все другие зависимости были зарегистрированы.  
---|---  
[Initialize](M_Tessa_Platform_ITessaServerDependencies_Initialize.htm)|
Выполняет инициализацию зависимостей платформы. Метод вызывается один раз при
запуске приложения.  
[RegisterCompilation](M_Tessa_Platform_ITessaServerDependencies_RegisterCompilation.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
регистрации API компиляции, вызываемом на сервере. Метод вызывается после
того, как все другие типовые зависимости были зарегистрированы.  
[RegisterCryptoAPI](M_Tessa_Platform_ITessaServerDependencies_RegisterCryptoAPI.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
регистрации криптографических API, вызываемых на сервере. Метод вызывается
после того, как все другие типовые зависимости были зарегистрированы.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
