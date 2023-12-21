# ITearDownPolicy - интерфейс
Политика освобождения ресурсов, занятых экземплярами расширений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITearDownPolicy : IExtensionPolicy
VB __Копировать
     Public Interface ITearDownPolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class ITearDownPolicy : IExtensionPolicy
F# __Копировать
     type ITearDownPolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Методы
[TearDownAsync](M_Tessa_Extensions_ITearDownPolicy_TearDownAsync.htm)|
Освобождает ресурсы, занятые заданным экземпляром расширений.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
