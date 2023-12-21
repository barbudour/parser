# IExtensionAssemblyInfo.Register - метод
Регистрирует сборку расширений с указанием места её использования.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IExtensionAssemblyInfo Register(
    	SessionType sessionType,
    	ExtensionAssembly assembly
    )
VB __Копировать
     Function Register ( 
    	sessionType As SessionType,
    	assembly As ExtensionAssembly
    ) As IExtensionAssemblyInfo
C++ __Копировать
    IExtensionAssemblyInfo^ Register(
    	SessionType sessionType, 
    	ExtensionAssembly^ assembly
    )
F# __Копировать
     abstract Register : 
            sessionType : SessionType * 
            assembly : ExtensionAssembly -> IExtensionAssemblyInfo 
#### Параметры
sessionType [SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
    Место использования сборки расширений: на клиенте или на сервере.
assembly [ExtensionAssembly](T_Tessa_Extensions_ExtensionAssembly.htm)
    Информация по сборке расширений.
#### Возвращаемое значение
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[IExtensionAssemblyInfo - ](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
