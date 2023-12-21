# ImplicitUseKindFlags - перечисление
The implicit use kind flags.
## __Definition
 **Пространство имён:**
[Tessa.Properties.Resharper](N_Tessa_Properties_Resharper.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum ImplicitUseKindFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration ImplicitUseKindFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class ImplicitUseKindFlags
F# __Копировать
     [<FlagsAttribute>]
    type ImplicitUseKindFlags
##  __Члены
Access| 1|  Only entity marked with attribute considered used  
---|---|---  
Assign| 2|  Indicates implicit assignment to a member  
InstantiatedWithFixedConstructorSignature| 4|  Indicates implicit
instantiation of a type with fixed constructor signature. That means any
unused constructor parameters won't be reported as such.  
Default| 7|  The default.  
InstantiatedNoFixedConstructorSignature| 8|  Indicates implicit instantiation
of a type  
## __См. также
#### Ссылки
[Tessa.Properties.Resharper - пространство
имён](N_Tessa_Properties_Resharper.htm)
