# ImplicitUseTargetFlags - перечисление
Specify what is considered used implicitly when marked with
[MeansImplicitUseAttribute](T_Tessa_Properties_Resharper_MeansImplicitUseAttribute.htm)
or
[UsedImplicitlyAttribute](T_Tessa_Properties_Resharper_UsedImplicitlyAttribute.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Properties.Resharper](N_Tessa_Properties_Resharper.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum ImplicitUseTargetFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration ImplicitUseTargetFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class ImplicitUseTargetFlags
F# __Копировать
     [<FlagsAttribute>]
    type ImplicitUseTargetFlags
##  __Члены
Default| 1|  The default.  
---|---|---  
Itself| 1|  The itself.  
Members| 2|  Members of entity marked with attribute are considered used  
WithMembers| 3|  Entity marked with attribute and all its members considered
used  
## __См. также
#### Ссылки
[Tessa.Properties.Resharper - пространство
имён](N_Tessa_Properties_Resharper.htm)
