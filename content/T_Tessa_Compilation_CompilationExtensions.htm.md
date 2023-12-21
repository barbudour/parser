# CompilationExtensions - класс
Методы-расширения для пространства имён Tessa.Compilation.
## __Definition
 **Пространство имён:** [Tessa.Compilation](N_Tessa_Compilation.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CompilationExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class CompilationExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class CompilationExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type CompilationExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CompilationExtensions
##  __Методы
[RegisterCompilation](M_Tessa_Compilation_CompilationExtensions_RegisterCompilation.htm)|
Выполняет регистрацию API компилятора, доступную на сервере.  
---|---  
[Resolve<T>](M_Tessa_Compilation_CompilationExtensions_Resolve__1.htm)|  Найти
в результате сборки тип, реализующий интерфейс T и создать его экземпляр В
случае отсутствия хотя бы одного типа в сборке будет выброшено
System.InvalidOperationException  
[ResolveAll<T>](M_Tessa_Compilation_CompilationExtensions_ResolveAll__1.htm)|
Найти в результате сборки все типы, реализующие интерфейс T и создать их
экземпляры  
## __См. также
#### Ссылки
[Tessa.Compilation - пространство имён](N_Tessa_Compilation.htm)
