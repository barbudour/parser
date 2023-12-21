# TessaApplicationClientAddressGenerator.GetNextServiceAddress - метод
Возвращает адрес сервиса
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override string GetNextServiceAddress(
    	Object sender,
    	string handlerType
    )
VB __Копировать
     Public Overrides Function GetNextServiceAddress ( 
    	sender As Object,
    	handlerType As String
    ) As String
C++ __Копировать
     public:
    virtual String^ GetNextServiceAddress(
    	Object^ sender, 
    	String^ handlerType
    ) override
F# __Копировать
     abstract GetNextServiceAddress : 
            sender : Object * 
            handlerType : string -> string 
    override GetNextServiceAddress : 
            sender : Object * 
            handlerType : string -> string 
#### Параметры
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, запрашивающий адрес. Может быть равен null.
handlerType [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тип обработчика.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Адрес сервиса.
#### Реализации
[IHostServiceAddressGenerator.GetNextServiceAddress(Object,
String)](M_Tessa_Host_IHostServiceAddressGenerator_GetNextServiceAddress.htm)  
##  __См. также
#### Ссылки
[TessaApplicationClientAddressGenerator -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationClientAddressGenerator.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
