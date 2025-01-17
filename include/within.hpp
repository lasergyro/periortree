#ifndef PERIOR_TREE_WITHIN
#define PERIOR_TREE_WITHIN
#include "boundary_conditions.hpp"
#include "rectangle.hpp"
#include <cmath>

namespace perior
{

template<typename pointT, template<typename> class boundaryT>
inline typename boost::enable_if<traits::is_point<pointT>, bool>::type
within(const rectangle<pointT>& inner, const rectangle<pointT>& outer,
       const boundaryT<pointT>& b)
    BOOST_NOEXCEPT_OR_NOTHROW
{
    const pointT dc(restrict_direction(outer.center - inner.center, b));
    for(std::size_t i=0; i<traits::dimension<pointT>::value; ++i)
    {
        if(std::abs(dc[i]) > outer.radius[i] - inner.radius[i])
        {
            return false;
        }
    }
    return true;
}

template<typename pointT, template<typename> class boundaryT>
inline typename boost::enable_if<traits::is_point<pointT>, bool>::type
within(const pointT& p, const rectangle<pointT>& r, const boundaryT<pointT>& b)
    BOOST_NOEXCEPT_OR_NOTHROW
{
    const pointT dc(restrict_direction(p - r.center, b));
    for(std::size_t i=0; i<traits::dimension<pointT>::value; ++i)
    {
        if(std::abs(dc[i]) > r.radius[i])
        {
            return false;
        }
    }
    return true;
}

} // perior
#endif// PERIOR_TREE_BOUNDARY_CONDITIONS
