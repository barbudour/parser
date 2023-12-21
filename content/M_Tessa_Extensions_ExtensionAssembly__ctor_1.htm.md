# ExtensionAssembly(String, Version) - конструктор
Создаёт экземпляр класса с указанием значений его свойств. При этом ссылка на
сборку недоступна для свойства
[Assembly](P_Tessa_Extensions_ExtensionAssembly_Assembly.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ExtensionAssembly(
    	string assemblyName,
    	Version version
    )
VB __Копировать
     Public Sub New ( 
    	assemblyName As String,
    	version As Version
    )
C++ __Копировать
     public:
    ExtensionAssembly(
    	String^ assemblyName, 
    	Version^ version
    )
F# __Копировать
     new : 
            assemblyName : string * 
            version : Version -> ExtensionAssembly
#### Параметры
assemblyName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя сборки с расширениями. Не равно null или пустой строке.
version [Version](https://learn.microsoft.com/dotnet/api/system.version)
    Версия сборки с расширениями. Не равна null.
##  __См. также
#### Ссылки
[ExtensionAssembly - ](T_Tessa_Extensions_ExtensionAssembly.htm)
[ExtensionAssembly -
перегрузка](Overload_Tessa_Extensions_ExtensionAssembly__ctor.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
